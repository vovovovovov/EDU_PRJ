import HttpInstance from "@/utils/http";

export function getAPI () {
  return HttpInstance({
    url: 'test_url'
  })
}