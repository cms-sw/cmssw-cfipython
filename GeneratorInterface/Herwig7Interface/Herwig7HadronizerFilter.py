import FWCore.ParameterSet.Config as cms

def Herwig7HadronizerFilter(**kwargs):
  mod = cms.EDFilter('Herwig7HadronizerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
