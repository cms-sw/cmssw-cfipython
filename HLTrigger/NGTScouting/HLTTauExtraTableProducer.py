import FWCore.ParameterSet.Config as cms

def HLTTauExtraTableProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTTauExtraTableProducer',
    tableName = cms.string('hltHpsPFTau'),
    skipNonExistingSrc = cms.bool(False),
    taus = cms.InputTag(''),
    tauTransverseImpactParameters = cms.InputTag(''),
    deepTauVSe = cms.InputTag(''),
    deepTauVSmu = cms.InputTag(''),
    deepTauVSjet = cms.InputTag(''),
    precision = cms.int32(7),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
