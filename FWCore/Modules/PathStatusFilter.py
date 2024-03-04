import FWCore.ParameterSet.Config as cms

def PathStatusFilter(**kwargs):
  mod = cms.EDFilter('PathStatusFilter',
    logicalExpression = cms.string(''),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
