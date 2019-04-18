import FWCore.ParameterSet.Config as cms

simpleHbhereco = cms.EDProducer('HcalSimpleReconstructor',
  pedestalSubtractionType = cms.int32(1),
  pedestalUpperLimit = cms.double(2.7),
  timeSlewParsType = cms.int32(3),
  timeSlewPars = cms.vdouble(
    12.2999,
    -2.19142,
    0,
    12.2999,
    -2.19142,
    0,
    12.2999,
    -2.19142,
    0
  ),
  respCorrM3 = cms.double(0.95)
)
