import FWCore.ParameterSet.Config as cms

def BeamSpotWrite2DB(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamSpotWrite2DB',
    OutputFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
