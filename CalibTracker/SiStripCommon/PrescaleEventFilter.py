import FWCore.ParameterSet.Config as cms

def PrescaleEventFilter(*args, **kwargs):
  mod = cms.EDFilter('PrescaleEventFilter',
    prescale = cms.uint32(1),
    offset = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
