import FWCore.ParameterSet.Config as cms

def TotemRPLocalTrackFitter(**kwargs):
  mod = cms.EDProducer('TotemRPLocalTrackFitter',
    tagUVPattern = cms.InputTag('totemRPUVPatternFinder'),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
