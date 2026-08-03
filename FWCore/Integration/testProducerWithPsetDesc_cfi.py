import FWCore.ParameterSet.Config as cms

from .ProducerWithPSetDesc import ProducerWithPSetDesc

testProducerWithPsetDesc = ProducerWithPSetDesc(

  p_int = 2147483647,
  vfloatv2 = [1e+30]
)
