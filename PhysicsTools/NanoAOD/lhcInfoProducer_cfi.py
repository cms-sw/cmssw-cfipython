import FWCore.ParameterSet.Config as cms

lhcInfoProducer = cms.EDProducer('LHCInfoProducer',
  mightGet = cms.optional.untracked.vstring
)
