import FWCore.ParameterSet.Config as cms

l1GTAlgoBlockProducer = cms.EDProducer('L1GTAlgoBlockProducer',
  algorithms = cms.required.VPSet,
  mightGet = cms.optional.untracked.vstring
)
