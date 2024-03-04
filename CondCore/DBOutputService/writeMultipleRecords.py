import FWCore.ParameterSet.Config as cms

def writeMultipleRecords(**kwargs):
  mod = cms.EDAnalyzer('writeMultipleRecords',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
