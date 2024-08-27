import FWCore.ParameterSet.Config as cms

def CandMCMatchTableProducer(**kwargs):
  mod = cms.EDProducer('CandMCMatchTableProducer',
    objName = cms.required.string,
    branchName = cms.required.string,
    docString = cms.required.string,
    src = cms.required.InputTag,
    mcMap = cms.required.InputTag,
    objType = cms.required.string,
    mcMapVisTau = cms.optional.InputTag,
    mcMapDressedLep = cms.optional.InputTag,
    mapTauAnc = cms.optional.InputTag,
    genparticles = cms.optional.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
