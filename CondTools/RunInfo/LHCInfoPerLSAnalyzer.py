import FWCore.ParameterSet.Config as cms

def LHCInfoPerLSAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerLSAnalyzer',
    csvFormat = cms.untracked.bool(False),
    header = cms.untracked.bool(False),
    separator = cms.untracked.string(','),
    iov = cms.untracked.uint64(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
