import FWCore.ParameterSet.Config as cms

def SiStripSpyEventMatcherModule(**kwargs):
  mod = cms.EDFilter('SiStripSpyEventMatcherModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod