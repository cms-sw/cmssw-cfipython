import FWCore.ParameterSet.Config as cms

def DTDeadFlagPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTDeadFlagPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
