import FWCore.ParameterSet.Config as cms

def EtlDigiHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EtlDigiHitsValidation',
    folder = cms.string('MTD/ETL/DigiHits'),
    inputTag = cms.InputTag('mix', 'FTLEndcap'),
    optionalPlots = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
