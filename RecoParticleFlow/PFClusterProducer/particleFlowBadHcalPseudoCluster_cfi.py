import FWCore.ParameterSet.Config as cms

particleFlowBadHcalPseudoCluster = cms.EDProducer('PFBadHcalPseudoClusterProducer',
  enable = cms.bool(True),
  debug = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
