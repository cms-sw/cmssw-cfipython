import FWCore.ParameterSet.Config as cms

def PathStatusFilter(*args, **kwargs):
  mod = cms.EDFilter('PathStatusFilter',
    logicalExpression = cms.string(''),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
