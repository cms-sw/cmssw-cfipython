import FWCore.ParameterSet.Config as cms

def PrescaleEventFilter(**kwargs):
  mod = cms.EDFilter('PrescaleEventFilter',
    prescale = cms.uint32(1),
    offset = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
