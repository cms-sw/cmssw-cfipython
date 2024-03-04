import FWCore.ParameterSet.Config as cms

def EcalExclusiveTrigFilter(**kwargs):
  mod = cms.EDFilter('EcalExclusiveTrigFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
