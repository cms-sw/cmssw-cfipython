import FWCore.ParameterSet.Config as cms

def CSCDDUMapPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCDDUMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
