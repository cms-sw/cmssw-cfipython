import FWCore.ParameterSet.Config as cms

def SignallingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SignallingAnalyzer',
    signal = cms.untracked.string('INT'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
