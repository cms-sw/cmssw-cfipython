import FWCore.ParameterSet.Config as cms

def AlCaIsolatedBunchSelector(*args, **kwargs):
  mod = cms.EDFilter('AlCaIsolatedBunchSelector',
    triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
    processName = cms.string('HLT'),
    triggerName = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
