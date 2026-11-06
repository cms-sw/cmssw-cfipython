import FWCore.ParameterSet.Config as cms

def EtlDigiSoAHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EtlDigiSoAHitsValidation',
    folder = cms.string('MTD/ETL/DigiHitsSoA'),
    inputTag = cms.InputTag('etlDigiSoAProducer', 'MTDEndcapSoA'),
    optionalPlots = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
