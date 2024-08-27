import FWCore.ParameterSet.Config as cms

def SignallingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SignallingAnalyzer',
    signal = cms.untracked.string('INT'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
