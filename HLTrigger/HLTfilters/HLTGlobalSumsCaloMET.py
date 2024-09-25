import FWCore.ParameterSet.Config as cms

def HLTGlobalSumsCaloMET(*args, **kwargs):
  mod = cms.EDFilter('HLTGlobalSumsCaloMET',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltCollection'),
    triggerType = cms.int32(0),
    observable = cms.string(''),
    Min = cms.double(-1e+125),
    Max = cms.double(1e+125),
    MinN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
