import FWCore.ParameterSet.Config as cms

def L1CaloGeometryDump(**kwargs):
  mod = cms.EDAnalyzer('L1CaloGeometryDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
