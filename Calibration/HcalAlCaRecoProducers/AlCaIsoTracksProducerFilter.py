import FWCore.ParameterSet.Config as cms

def AlCaIsoTracksProducerFilter(**kwargs):
  mod = cms.EDFilter('AlCaIsoTracksProducerFilter',
    triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
    triggers = cms.vstring(
      'HLT_IsoTrackHB',
      'HLT_IsoTrackHE'
    ),
    processName = cms.string('HLT'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
