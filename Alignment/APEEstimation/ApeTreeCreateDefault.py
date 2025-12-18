import FWCore.ParameterSet.Config as cms

def ApeTreeCreateDefault(*args, **kwargs):
  mod = cms.EDAnalyzer('ApeTreeCreateDefault',
    resultFile = cms.string('defaultAPE.root'),
    trackerTreeFile = cms.required.string,
    sectors = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
