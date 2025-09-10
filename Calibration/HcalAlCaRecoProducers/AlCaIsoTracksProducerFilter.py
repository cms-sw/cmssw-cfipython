import FWCore.ParameterSet.Config as cms

def AlCaIsoTracksProducerFilter(*args, **kwargs):
  mod = cms.EDFilter('AlCaIsoTracksProducerFilter',
    triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
    triggers = cms.vstring(
      'HLT_IsoTrackHB',
      'HLT_IsoTrackHE'
    ),
    processName = cms.string('HLT'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
