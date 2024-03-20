import FWCore.ParameterSet.Config as cms

alpakaBackendProducer = cms.EDProducer('AlpakaBackendProducer@alpaka',
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
