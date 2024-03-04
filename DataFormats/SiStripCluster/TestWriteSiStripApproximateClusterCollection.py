import FWCore.ParameterSet.Config as cms

def TestWriteSiStripApproximateClusterCollection(**kwargs):
  mod = cms.EDProducer('TestWriteSiStripApproximateClusterCollection',
    integralValues = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
