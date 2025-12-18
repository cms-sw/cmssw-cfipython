import FWCore.ParameterSet.Config as cms

def DumpFEDRawDataProduct(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpFEDRawDataProduct',
    feds = cms.required.untracked.vint32,
    label = cms.required.untracked.InputTag,
    dumpPayload = cms.required.untracked.bool,
    usePhase2 = cms.required.untracked.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
