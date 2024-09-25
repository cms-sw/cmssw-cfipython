import FWCore.ParameterSet.Config as cms

def L1TDiffHarvesting(*args, **kwargs):
  mod = cms.EDProducer('L1TDiffHarvesting',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
