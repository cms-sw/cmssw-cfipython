import FWCore.ParameterSet.Config as cms

alcaIsoTracksProducerFilter = cms.EDFilter('AlCaIsoTracksProducerFilter',
  triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
  triggers = cms.vstring(
    'HLT_IsoTrackHB',
    'HLT_IsoTrackHE'
  ),
  processName = cms.string('HLT'),
  mightGet = cms.optional.untracked.vstring
)
