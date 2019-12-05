import FWCore.ParameterSet.Config as cms

JetCorrFactorsProducer = cms.EDProducer('JetCorrFactorsProducer',
  emf = cms.bool(False),
  flavorType = cms.string('J'),
  src = cms.InputTag('ak5CaloJets'),
  payload = cms.string('AK5Calo'),
  useNPV = cms.bool(True),
  primaryVertices = cms.InputTag('offlinePrimaryVertices'),
  useRho = cms.bool(True),
  rho = cms.InputTag('kt6PFJets', 'rho'),
  levels = cms.vstring(
    'L1Offset',
    'L2Relative',
    'L3Absolute',
    'L5Flavor',
    'L7Parton'
  )
)
