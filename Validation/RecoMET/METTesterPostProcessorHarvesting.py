import FWCore.ParameterSet.Config as cms

def METTesterPostProcessorHarvesting(*args, **kwargs):
  mod = cms.EDProducer('METTesterPostProcessorHarvesting',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
