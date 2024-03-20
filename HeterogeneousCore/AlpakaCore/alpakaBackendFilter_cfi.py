import FWCore.ParameterSet.Config as cms

alpakaBackendFilter = cms.EDFilter('AlpakaBackendFilter',
  producer = cms.InputTag('alpakaBackendProducer', 'backend'),
  backends = cms.vstring('SerialSync'),
  mightGet = cms.optional.untracked.vstring
)
