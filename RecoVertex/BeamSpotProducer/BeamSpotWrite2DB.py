import FWCore.ParameterSet.Config as cms

def BeamSpotWrite2DB(**kwargs):
  mod = cms.EDAnalyzer('BeamSpotWrite2DB',
    OutputFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
