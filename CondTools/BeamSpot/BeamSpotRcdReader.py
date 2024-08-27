import FWCore.ParameterSet.Config as cms

def BeamSpotRcdReader(**kwargs):
  mod = cms.EDAnalyzer('BeamSpotRcdReader',
    rawFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
