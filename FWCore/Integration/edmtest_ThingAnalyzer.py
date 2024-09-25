import FWCore.ParameterSet.Config as cms

def edmtest_ThingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::ThingAnalyzer',
    beginRun = cms.untracked.InputTag('thing', 'beginRun'),
    beginLumi = cms.untracked.InputTag('thing', 'beginLumi'),
    event = cms.untracked.InputTag('thing'),
    endLumi = cms.untracked.InputTag('thing', 'endLumi'),
    endRun = cms.untracked.InputTag('thing', 'endRun'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
