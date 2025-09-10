import FWCore.ParameterSet.Config as cms

def TestWriteSiStripApproximateClusterCollection(*args, **kwargs):
  mod = cms.EDProducer('TestWriteSiStripApproximateClusterCollection',
    integralValues = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
