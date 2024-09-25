import FWCore.ParameterSet.Config as cms

def DisplayGeom(*args, **kwargs):
  mod = cms.EDAnalyzer('DisplayGeom',
    nodes = cms.untracked.vstring(
      'tracker:Tracker_1',
      'muonBase:MUON_1',
      'caloBase:CALO_1'
    ),
    level = cms.untracked.int32(4),
    MF_component = cms.untracked.string('None'),
    MF_plane_d0 = cms.untracked.vdouble(
      0,
      -900,
      -2400
    ),
    MF_plane_d1 = cms.untracked.vdouble(
      0,
      -900,
      2400
    ),
    MF_plane_d2 = cms.untracked.vdouble(
      0,
      900,
      -2400
    ),
    MF_plane_N = cms.untracked.int32(200),
    MF_plane_N2 = cms.untracked.int32(-1),
    MF_plane_draw_dir = cms.untracked.int32(1),
    MF_pickable = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
