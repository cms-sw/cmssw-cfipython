import FWCore.ParameterSet.Config as cms

def HcalLutAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalLutAnalyzer',
    inputDir = cms.string('conditions'),
    plotsDir = cms.string('conditions/Figures'),
    tags = cms.vstring(
      'tag1',
      'tag2'
    ),
    quality = cms.vstring(
      '0',
      '999999'
    ),
    pedestals = cms.vstring(
      '0',
      '999999'
    ),
    effpedestals = cms.vstring(
      '0',
      '999999'
    ),
    gains = cms.vstring(
      '0',
      '999999'
    ),
    respcorrs = cms.vstring(
      '0',
      '999999'
    ),
    Zmin = cms.double(0),
    Zmax = cms.double(10),
    Ymin = cms.double(0.7),
    Ymax = cms.double(1.3),
    Pmin = cms.double(0.9),
    Pmax = cms.double(1.1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
