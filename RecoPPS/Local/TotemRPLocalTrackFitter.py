import FWCore.ParameterSet.Config as cms

def TotemRPLocalTrackFitter(*args, **kwargs):
  mod = cms.EDProducer('TotemRPLocalTrackFitter',
    tagUVPattern = cms.InputTag('totemRPUVPatternFinder'),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
