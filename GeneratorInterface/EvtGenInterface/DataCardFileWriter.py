import FWCore.ParameterSet.Config as cms

def DataCardFileWriter(**kwargs):
  mod = cms.EDAnalyzer('DataCardFileWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
