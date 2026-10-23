import FWCore.ParameterSet.Config as cms

def BTagSkimMC(*args, **kwargs):
  mod = cms.EDFilter('BTagSkimMC',
    mcProcess = cms.string('ttbar'),
    pthat_min = cms.double(50),
    verbose = cms.untracked.bool(False),
    pthat_max = cms.double(80),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
