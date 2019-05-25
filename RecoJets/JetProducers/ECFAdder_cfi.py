import FWCore.ParameterSet.Config as cms

ECFAdder = cms.EDProducer('ECFAdder',
  src = cms.InputTag('no default'),
  Njets = cms.vuint32(
    1,
    2,
    3
  ),
  cuts = cms.vstring(
    '',
    '',
    ''
  ),
  alpha = cms.double(1),
  beta = cms.double(1),
  ecftype = cms.string('')
)
