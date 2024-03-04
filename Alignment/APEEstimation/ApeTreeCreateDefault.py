import FWCore.ParameterSet.Config as cms

def ApeTreeCreateDefault(**kwargs):
  mod = cms.EDAnalyzer('ApeTreeCreateDefault',
    resultFile = cms.string('defaultAPE.root'),
    trackerTreeFile = cms.required.string,
    sectors = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
