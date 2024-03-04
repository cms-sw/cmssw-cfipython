import FWCore.ParameterSet.Config as cms

def ExternalLHEAsciiDumper(**kwargs):
  mod = cms.EDAnalyzer('ExternalLHEAsciiDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
