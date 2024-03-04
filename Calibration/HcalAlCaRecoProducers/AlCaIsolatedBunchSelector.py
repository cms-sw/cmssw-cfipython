import FWCore.ParameterSet.Config as cms

def AlCaIsolatedBunchSelector(**kwargs):
  mod = cms.EDFilter('AlCaIsolatedBunchSelector',
    triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
    processName = cms.string('HLT'),
    triggerName = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
