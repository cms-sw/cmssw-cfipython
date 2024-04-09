import FWCore.ParameterSet.Config as cms

def CSCReadoutMapTest(**kwargs):
  mod = cms.EDAnalyzer('CSCReadoutMapTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod