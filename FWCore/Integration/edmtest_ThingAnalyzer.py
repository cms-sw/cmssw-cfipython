import FWCore.ParameterSet.Config as cms

def edmtest_ThingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::ThingAnalyzer',
    beginRun = cms.untracked.InputTag('thing', 'beginRun'),
    beginLumi = cms.untracked.InputTag('thing', 'beginLumi'),
    event = cms.untracked.InputTag('thing'),
    endLumi = cms.untracked.InputTag('thing', 'endLumi'),
    endRun = cms.untracked.InputTag('thing', 'endRun'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
